<template>
    <div class="autocomplete">
        <input id="inputName" v-model="search" @input="onChange" type="text"/>
        <ul v-show="isOpen" class="autocomplete-results">
            <li @click="setResult(result)" v-for="(result, i) in results" :key="i" class="autocomplete-result">
                {{ result.nama }}
            </li>
        </ul>
    </div>
</template>
<style>
  .autocomplete {
    position: relative;
  }

  .autocomplete-results {
    padding: 0;
    margin: 0;
    border: 1px solid #eeeeee;
    height: 50px;
    min-height: 1em;
    max-height: 6em;    
    overflow: auto;
  }

  .autocomplete-result {
    list-style: none;
    text-align: left;
    padding: 4px 2px;
    cursor: pointer;
  }

  .autocomplete-result:hover {
    background-color: #4AAE9B;
    color: white;
  }
</style>
<script>

export default {
    name: 'SearchAutocomplete',
    mounted() {
        document.addEventListener('click', this.handleClickOutside);
    },
    unmounted() {
        document.removeEventListener('click', this.handleClickOutside);
    },
    props: {
        items: {
            type: Array,
            required: false,
            default: () => [],
        },
    },
    data() {
        return {
            search: '',
            selectedId: null,
            results: [],
            isOpen: false,
        };
    },
    methods: {
        filterResults() {
            this.results = this.items.filter(item => item.nama.toLowerCase().indexOf(this.search.toLowerCase()) > -1);
        },
        onChange() {
            this.filterResults();
            this.isOpen = true;
        },
        setResult(result) {
            this.search = result.nama;
            this.isOpen = false;
            this.selectedId = result.id_jemaat;
            this.$emit('itemselected', this.selectedId)
            console.log('selectedId', this.selectedId)
        },
        handleClickOutside(event) {
            if (!this.$el.contains(event.target)) {
                this.isOpen = false;
            }
        }
    },
};
</script>