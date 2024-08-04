<template>
  <div class="full-width row items-center justify-between">
    <p class="fs-16 font-semibold">Личный кабинет</p>

    <div v-if="profileStore.isProfileLoaded" class="">
      <p>
        <span class="font-semibold fs-16">Баланс {{ toMoney(profile.balance) }}₽</span>
        /
        <span class="font-light">{{ toMoney(profile.spentBalance) }}₽</span>
      </p>
    </div>
    <q-skeleton v-else type="text" width="170px" height="40px" />
  </div>
</template>

<script>
import { useProfileStore } from 'src/stores/profile'
import { toMoney } from 'src/utils/formatters'

export default {
  name: 'ProjectsPageToolbarContent',
  data() {
    return {
      profileStore: useProfileStore(),
    }
  },
  computed: {
    profile() {
      return this.profileStore.profile
    },
  },
  mounted() {
    if (!this.profileStore.isProfileLoaded) {
      this.profileStore.loadProfile()
    }
  },
  methods: { toMoney },
}
</script>
