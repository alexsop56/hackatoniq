<template>
  <q-expansion-item class="q-ma-sm bg-white br-10 overflow-hidden">
    <template v-slot:header>
      <div class="row justify-between full-width q-pr-md q-pr-md-none">
        <!-- Дата начала задания -->
        <div class="col-12 col-md-2">
          <div class="row items-center">
            <q-icon name="schedule" size="20px" color="primary" class="q-mr-xs" />

            <span class="item-secondary-text">{{ item.startTime }}</span>
          </div>

          <div class="row items-center">
            <q-icon name="calendar_month" size="20px" color="primary" class="q-mr-xs" />

            <span class="item-secondary-text">{{ item.startDate }}</span>
          </div>
        </div>

        <!-- Адрес -->
        <div class="col-12 col-md-3 row items-center no-wrap q-mt-sm q-mt-md-none">
          <q-icon name="pin_drop" size="20px" color="primary" class="q-mr-xs" />

          <span class="item-secondary-text">
            {{ item.address }}
          </span>
        </div>

        <!-- Количество исполнителей и просмотров -->
        <div class="col-md-3 column q-mt-sm q-mt-md-none">
          <div class="row items-center">
            <q-icon name="person" size="20px" color="primary" class="q-mr-xs" />

            <span class="item-secondary-text text-red">
              Исполнителей {{ item.workersCount }} / {{ item.workersRequiredCount }}
            </span>
          </div>

          <div class="row items-center">
            <q-icon name="visibility" size="20px" color="primary" class="q-mr-xs" />

            <span class="item-secondary-text">Просмотров {{ item.views }}</span>
          </div>
        </div>

        <!-- Ставка -->
        <div class="col-md-3 column q-mt-sm q-mt-md-none">
          <div class="row items-center">
            <q-icon name="account_balance_wallet" size="20px" color="primary" class="q-mr-xs" />

            <span class="item-secondary-text">Ставка {{ item.price }} ₽</span>
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
<style lang="scss" scoped>
@import 'src/css/quasar.variables.scss';
@import 'src/css/app.scss';

.item-secondary-text {
  color: $secondary;
  font-family: $font-family-inter-light;
  font-size: 12px;
}
</style>
