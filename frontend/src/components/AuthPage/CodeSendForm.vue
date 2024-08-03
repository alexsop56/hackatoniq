<template>
  <q-card class="q-pa-lg">
    <div class="text-center">
      <span class="q-ml-md q-my-none fs-30 text-accent">Selling</span>
      <span class="fs-30 text-primary">Force</span>
    </div>

    <q-input
      dense
      class="q-mt-sm"
      input-class="text-accent"
      color="primary"
      placeholder="E-mail"
      v-model="store.email"
      :error="store.emailError"
      hide-bottom-space
      @keyup.enter="sendCode"
    />

    <q-btn
      :loading="store.loading"
      rounded
      no-caps
      class="q-py-sm full-width q-mt-md"
      color="primary"
      label="Получить код"
      @click="sendCode"
    />

    <p class="font-size-10 text-center q-mt-md">
      Вводя E-mail, вы подтверждаете согласие с
      <a href="oferta" target="_blank">публичной офертой</a>
      и
      <br />
      <a href="policy" target="_blank">политикой конфиденциальности</a>
    </p>
  </q-card>
</template>

<script>
import { useAuthStore } from 'stores/auth'

export default {
  name: 'CodeSendForm',
  data() {
    return {
      store: useAuthStore(),
    }
  },
  methods: {
    sendCode() {
      if (this.store.email?.length > 5) {
        this.store.sendCode()
      }
    },
  },
}
</script>
