from app import create_app
import os
import threading

app = create_app()

def run_npm_serve():
    print("Running npm serve function...")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    frontend_dir = os.path.join(current_dir,'frontend')
    print(frontend_dir)
    if not os.path.isdir(frontend_dir):
        print(f"Error: Directory '{frontend_dir}' not found.")
    os.chdir(frontend_dir)
    return os.system('npm run serve')

def run_flask_app():
    print("Running Flask app...")
    app.run(port=5000, debug=True,use_reloader=False)
    
if __name__ == '__main__':
    # Create threads for each function
    npm_thread = threading.Thread(target=run_npm_serve)
    flask_thread = threading.Thread(target=run_flask_app)

    # Start both threads
    npm_thread.start()
    flask_thread.start()

    # Wait for both threads to finish
    npm_thread.join()
    flask_thread.join()
