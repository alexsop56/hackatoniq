import { defineStore } from 'pinia'
import Profile from 'src/models/Profile/Profile'
import AuthApi from 'src/services/api/AuthApi'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    profile: new Profile(),
  }),
  getters: {
    isProfileLoaded: state => state.profile?.id,
  },
  actions: {
    loadProfile() {
      AuthApi.getMe().then(response => {
        this.profile = new Profile(response.data)
      })
    },
  },
})
