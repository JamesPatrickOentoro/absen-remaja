<template>
    <nav class="navbar navbar-expand-sm bg-body-tertiary" id="header-nav" style="box-shadow: rgba(0, 0, 0, .06) 0 0 6px 2px;">
        <div class="container-fluid">
            <a class="navbar-brand">Dashboard</a>
            <form class="d-flex" role="search">
                <router-link to="/admin-view"><button class="btn btn-outline-success" type="submit">Admin
                        Login</button></router-link>
            </form>
        </div>
    </nav>
</template>


<script>
export default {
    name: 'HeaderBefore',
}

</script>


<style></style>