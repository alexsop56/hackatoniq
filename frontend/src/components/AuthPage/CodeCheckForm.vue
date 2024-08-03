<template>
  <q-card class="q-pa-lg">
    <div class="text-center">
      <span class="q-ml-md q-my-none fs-30 text-accent">Selling</span>
      <span class="fs-30 text-primary">Force</span>
    </div>

    <p class="text-center q-my-sm">
      Код отправлен на E-mail
      <b>{{ store.email }}</b>
    </p>

    <div class="width-fit-content q-mx-auto">
      <q-input
        dense
        input-class="sms-code-input"
        placeholder="_ _ _ _ _"
        color="primary"
        v-model="code"
        @keyup="filterChars"
        hide-bottom-space
        maxlength="5"
        @keyup.enter="store.checkCode(code)"
      />

      <q-btn
        color="primary"
        no-caps
        rounded
        class="full-width q-mt-md q-mb-xs"
        label="Подтвердить"
        @click="store.checkCode(code)"
      />
      <q-btn flat rounded no-caps class="full-width" color="primary" label="Изменить E-mail" @click="store.logout" />
    </div>
  </q-card>
</template>

<script>
import { useAuthStore } from 'stores/auth'

export default {
  name: 'CodeCheckForm',
  data() {
    return {
      store: useAuthStore(),

      code: '',
    }
  },
  methods: {
    filterChars() {
      if (!this.code) {
        return
      }

      this.code = this.code.toString().replace(/\D/g, '')
    },
  },
}
</script>
<style>
.sms-code-input {
  color: white;
  letter-spacing: 8px;
  text-align: center;
}
</style>
