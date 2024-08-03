<template>
  <div class="h-100vh w-100 flex-center column">
    <transition name="fade" mode="out-in">
      <sms-send-form v-if="!store.isSmsSent" />
      <sms-check-form v-else-if="store.isSmsSent" />
    </transition>
  </div>
</template>

<script>
import { useAuthStore } from 'stores/auth'

import SmsCheckForm from 'src/components/AuthPage/CodeCheckForm.vue'
import SmsSendForm from 'src/components/AuthPage/CodeSendForm.vue'

export default {
  data() {
    return {
      store: useAuthStore(),
    }
  },
  components: {
    SmsCheckForm,
    SmsSendForm,
  },
}
</script>

<style scoped>
.fade-enter-active {
  transition: all 0.3s ease-out;
}

.fade-leave-active {
  transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1);
}

.fade-enter-from,
.fade-leave-to {
  transform: translateY(20px);
  opacity: 0;
}
</style>
