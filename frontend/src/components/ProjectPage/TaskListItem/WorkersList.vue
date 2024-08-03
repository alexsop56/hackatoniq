<template>
  <q-card>
    <q-card-section>
      <div class="row">
        <div
          class="text-center font-semibold"
          :class="'col-' + column.col"
          v-for="column in columns"
          :key="column.title"
        >
          {{ column.label }}
        </div>
      </div>

      <div class="row items-center worker-item" v-for="worker in workers" :key="worker.id">
        <div class="text-center q-pa-xs" :class="'col-' + column.col" v-for="column in columns" :key="column.title">
          {{ worker[column.title] }}
        </div>
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  name: 'WorkersList',
  props: {
    workers: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      columns: [
        {
          label: 'ФИО',
          title: 'fullName',
          col: '4',
        },
        {
          label: 'Номер телефона',
          title: 'phone',
          col: '5',
        },
        {
          label: 'Рейтинг',
          title: 'rating',
          col: '3',
        },
      ],
    }
  },
}
</script>
<style lang="scss" scoped>
@import 'src/css/quasar.variables.scss';

.worker-item {
  border-radius: 10px;
  background-color: $bg-bright;
  padding: 5px;
  margin-top: 5px;
}
</style>
