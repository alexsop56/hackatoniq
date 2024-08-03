<template>
  <q-expansion-item class="q-ma-sm bg-white br-10 overflow-hidden">
    <template v-slot:header>
      <div class="column row-md justify-between items-md-center full-width q-pr-md q-pr-md-none">
        <!-- Дата начала задания -->
        <div class="col-md-2">
          <div class="row items-center">
            <q-icon name="schedule" size="20px" color="primary" class="q-mr-xs" />

            <span class="text-secondary font-light fs-12">{{ item.startTime }}</span>
          </div>

          <div class="row items-center">
            <q-icon name="calendar_month" size="20px" color="primary" class="q-mr-xs" />

            <span class="text-secondary font-light fs-12">{{ item.startDate }}</span>
          </div>
        </div>

        <!-- Адрес -->
        <div class="col-md-3 q-mt-md q-mt-md-none row items-center no-wrap">
          <q-icon name="pin_drop" size="24px" color="primary" class="q-mr-xs" />

          <span class="text-secondary font-light fs-12">
            {{ item.address }}
          </span>
        </div>

        <!-- Количество исполнителей и просмотров -->
        <div class="col-md-3 q-mt-md q-mt-md-none column">
          <div class="row items-center">
            <q-icon name="person" size="20px" color="primary" class="q-mr-xs" />

            <span class="text-secondary font-light fs-12 text-red">
              Исполнителей {{ item.workersCount }} / {{ item.workersRequiredCount }}
            </span>
          </div>

          <div class="row items-center">
            <q-icon name="visibility" size="20px" color="primary" class="q-mr-xs" />

            <span class="text-secondary font-light fs-12">Просмотров {{ item.views }}</span>
          </div>
        </div>

        <!-- Ставка -->
        <div class="col-md-3 column">
          <div class="row items-center">
            <q-icon name="account_balance_wallet" size="20px" color="primary" class="q-mr-xs" />

            <span class="text-secondary font-light fs-12">Ставка {{ item.price }} ₽</span>
          </div>
        </div>
      </div>
    </template>

    <!-- Раскрывающийся список работников -->
    <workers-list :workers="item.workers" />
  </q-expansion-item>
</template>

<script>
import WorkersList from './TaskListItem/WorkersList.vue'

export default {
  name: 'TaskListItem',
  components: {
    WorkersList,
  },
  props: {
    item: {
      type: Object,
      required: true,
    },
  },
}
</script>
