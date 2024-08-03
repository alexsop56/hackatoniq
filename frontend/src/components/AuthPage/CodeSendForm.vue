<template>
  <q-card class="q-pa-lg"></q-card>
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
