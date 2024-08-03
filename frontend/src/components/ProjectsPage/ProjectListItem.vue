<template>
  <q-item class="q-ma-sm bg-white br-10" :to="routeToProject" clickable>
    <div class="col-6 q-pa-sm">
      <p class="fs-18 text-bold">{{ item.title }}</p>

      <div class="column row-md items-md-center q-mt-sm">
        <div class="row items-start col-6">
          <p class="q-mr-xs font-light">Задания в работе</p>
          <p class="q-mr-xs font-light text-bold">{{ item.tasksCount }}</p>
        </div>

        <div class="row items-start col-6">
          <p class="q-mr-xs font-light">Набрано</p>
          <p class="q-mr-xs font-light text-bold">{{ item.workersCount }} / {{ item.workersRequiredCount }}</p>
        </div>
      </div>

      <div class="row q-mt-sm items-center">
        <q-icon name="pin_drop" size="24px" color="primary" />
        <p class="font-light">{{ item.address }}</p>
      </div>

      <div class="row items-center q-mt-sm">
        <div class="row items-center col-6">
          <q-icon name="priority_high" size="24px" color="red" />
          <b class="text-red">{{ item.attentionCount }}</b>
        </div>

        <div class="col-6">
          <q-btn flat rounded dense no-caps label="Cделать" color="red">
            <q-badge color="red" floating rounded transparent>{{ item.todoCount }}</q-badge>
          </q-btn>
        </div>
      </div>
    </div>
    <div class="col-6 column justify-center q-pa-sm">
      <order-progress-bar
        v-for="task in item.tasks"
        :key="task.id"
        class="q-mt-sm"
        :title="task.workTypeTitle"
        :value="task.workersCount"
        :max="task.workersRequiredCount"
      />
    </div>
  </q-item>
</template>

<script>
import OrderProgressBar from './OrderProgressBar.vue'

export default {
  name: 'ProjectListItem',
  components: {
    OrderProgressBar,
  },
  props: {
    item: {
      type: Object,
      required: true,
    },
  },
  computed: {
    routeToProject() {
      return '/projects/' + this.item.id
    },
  },
}
</script>
