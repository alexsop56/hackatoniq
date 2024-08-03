<template>
  <q-dialog v-model="modal.state" @hide="onModalHide">
    <q-card flat>
      <q-card-section>
        <p class="modal-header">Создание задания</p>
      </q-card-section>

      <q-card-section>
        <!-- Период, на который необходимо создать задания -->
        <!-- <q-input
          v-model="modal.form.period"
          bg-color="white"
          label-color="grey-3"
          label="Период, на который необходимо создать задания"
          :mask="$validation.modal.form.period.mask"
          v-replace-characters-for-mask="$validation.modal.form.period.mask"
          :error="v$.modal.form.period.$error"
          :error-message="v$.modal.form.period.$errors.at(-1)?.$message"
          @update:model-value="updateModel"
          clearable
        >
          <template #append>
            <q-icon name="event" class="cursor-pointer">
              <q-popup-proxy v-model="periodStateOfPicker" cover transition-show="scale" transition-hide="scale">
                <q-date
                  v-model="preparedPeriod"
                  color="main-theme"
                  text-color="accent-font"
                  range
                  :locale="$config.dateLocale"
                  :mask="$validation.date.format"
                  :subtitle="period ? undefined : ' '"
                  :title="period ? false : $t('field.periodSelect')"
                  @update:model-value="periodStateOfPicker = false"
                >
                  <div class="row items-center justify-end">
                    <q-btn v-close-popup label="Закрыть" color="accent-font" flat />
                  </div>
                </q-date>
              </q-popup-proxy>
            </q-icon>
          </template>
        </q-input> -->

        <!-- Ставка -->
        <q-input
          type="number"
          color="primary"
          label="Ставка"
          input-class="text-accent"
          label-color="secondary"
          v-model.number="modal.form.price"
          :error="v$.modal.form.price.$error"
          :error-message="v$.modal.form.price.$errors[0]?.$message"
          hide-bottom-space
          no-error-icon
        >
          <template v-slot:append>
            <q-icon name="currency_ruble" color="secondary" size="16px" />
          </template>
        </q-input>
      </q-card-section>

      <q-card-section>
        <q-btn
          class="full-width"
          color="primary"
          label="Создать"
          no-caps
          rounded
          @click="onCreate"
          :loading="modal.isLoading"
        />
      </q-card-section>
    </q-card>
  </q-dialog>
</template>

<script>
import { useVuelidate } from '@vuelidate/core'
import { required, minValue, maxValue, numeric } from 'src/utils/validators'
import { useTasksStore } from 'src/stores/tasks'

export default {
  name: 'TaskCreatingModal',

  data() {
    return {
      tasksStore: useTasksStore(),

      period: null,
      periodStateOfPicker: false,
    }
  },
  validations() {
    return {
      modal: {
        form: {
          price: { required, numeric, minValue: minValue(0), maxValue: maxValue(100000) },
        },
      },
    }
  },
  methods: {
    onCreate() {
      this.v$.$touch()

      if (this.v$.$error) return

      this.tasksStore.store().then(() => {
        this.modal.state = false
      })
    },
    onModalHide() {
      this.tasksStore.resetTaskModal()
    },
    updateModel() {
      this.v$.period.$touch()

      const period = this.parseRangeFromString(this.period)

      // Форматируем не через quasar data, потому что он не форматирует дату, если это 12 - 31 дни месяца (да да)
      // пробовал форматировать вот так date.formatToDashedDate(period.from, 'YYYY-MM-DD')

      this.registry.workStartDate = this.formatToDashedDate(period.from)
      this.registry.workEndDate = this.formatToDashedDate(period.to)
    },
  },
  computed: {
    modal() {
      return this.tasksStore.modals.task
    },
    preparedPeriod: {
      get() {
        return this.parseRangeFromString(this.period)
      },
      set(data) {
        this.period = data && data.from + ' - ' + data.to

        this.updateModel()
      },
    },
  },
  setup() {
    return {
      v$: useVuelidate(),
    }
  },
}
</script>
