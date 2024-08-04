<template>
  <div class="full-width">
    <div v-if="authStore.isProfileLoaded" class="row items-center justify-around">
      <p class="fs-18 font-semibold">Личный кабинет</p>

      <p>
        <span class="font-semibold fs-16">Баланс {{ toMoney(profile.balance) }}₽</span>
        /
        <span class="font-light">{{ toMoney(profile.spentBalance) }}₽</span>
      </p>
    </div>

    <q-skeleton v-else type="text" width="170px" height="40px" class="q-mx-auto" />
  </div>
</template>

<script>
import { useAuthStore } from 'src/stores/auth'
import { toMoney } from 'src/utils/formatters'

export default {
  name: 'ProjectsPageToolbarContent',
  data() {
    return {
      authStore: useAuthStore(),
    }
  },
  computed: {
    profile() {
      return this.authStore.profile
    },
  },
  mounted() {
    if (!this.authStore.isProfileLoaded) {
      this.authStore.loadProfile()
    }
  },
  methods: { toMoney },
}
</script>
