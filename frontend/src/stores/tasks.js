import { defineStore } from 'pinia'
import TaskListItem from 'src/models/Task/TaskListItem'
import TaskApi from 'src/services/api/TaskApi'

export const useTasksStore = defineStore('tasks', {
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
      return await TaskApi.index(page, this.itemsPerPage).then(response => {
        let data = response.data

        for (let item of data.items) {
          this.items.push(new TaskListItem(item))
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
