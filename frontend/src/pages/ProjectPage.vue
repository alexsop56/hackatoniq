<template>
  <q-page>
    <!-- Кнопка создания задания (когда список пуст)  -->
    <div class="row justify-center items-center flex-1" v-if="!tasksStore.items.length && !tasksStore.isLoading">
      <q-btn icon="construction" unelevated color="primary" no-caps rounded label="Создать задание" />
    </div>

    <div v-if="!tasksStore.items.length && tasksStore.isLoading">
      <task-list-item-skeleton v-for="skeletonIndex in skeletonsCount" :key="skeletonIndex" />
    </div>

    <!-- Список -->
    <q-infinite-scroll @load="onLoad">
      <task-list-item class="q-mb-sm" :item="item" v-for="item in tasksStore.items" :key="item.id" />

      <template v-slot:loading>
        <div class="row justify-center q-my-md">
          <q-spinner-oval color="primary" size="40px" />
        </div>
      </template>
    </q-infinite-scroll>
  </q-page>
</template>

<script>
import { useTasksStore } from 'stores/tasks'

import TaskListItem from 'src/components/ProjectPage/TaskListItem.vue'
import TaskListItemSkeleton from 'src/components/ProjectPage/TaskListItemSkeleton.vue'

export default {
  name: 'ProjectPage',
  components: {
    TaskListItem,
    TaskListItemSkeleton,
  },
  data() {
    return {
      tasksStore: useTasksStore(),

      skeletonsCount: 10,
    }
  },
  mounted() {
    this.tasksStore.resetList()
  },
  methods: {
    async onLoad(index, done) {
      this.tasksStore.isLoading = true

      this.tasksStore.loadList(index).then(() => {
        done(this.tasksStore.isAllItemsLoaded)

        this.tasksStore.isLoading = false
      })
    },
  },
}
</script>
