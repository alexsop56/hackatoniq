import { defineStore } from 'pinia'
import ProjectApi from 'src/services/api/ProjectApi'
import ProjectListItem from 'src/models/Project/ProjectListItem'

export const useProjectsStore = defineStore('projects', {
  state: () => ({
    items: [],
    isLoading: false,
    total: 0,
    itemsPerPage: 50,
  }),
  getters: {
    isAllItemsLoaded: state => {
      return state.items.length >= state.total
    },
  },
  actions: {
    async loadList(page) {
      // TODO
      return await ProjectApi.index(page, this.itemsPerPage).then(response => {
        let data = response.data

        for (let item of data.items) {
          this.items.push(new ProjectListItem(item))
        }

        this.total = data.total
      })
    },

    resetList() {
      this.items = []
      this.total = 0
    },
  },
})
