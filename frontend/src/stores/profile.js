import { defineStore } from 'pinia'
import Profile from 'src/models/Profile/Profile'
import ProfileApi from 'src/services/api/ProfileApi'
import { api } from 'src/boot/axios'

export const useProfileStore = defineStore('profile', {
  state: () => ({
    auth: {
      phone: null,
      code: null,
      isLoading: false,
      isSmsSent: false,
    },

    profile: new Profile(),
  }),
  getters: {
    isProfileLoaded: state => state.profile?.id,
  },
  actions: {
    loadProfile() {
      ProfileApi.getMe().then(response => {
        this.profile = new Profile(response.data)
      })
    },
    sendCode() {
      this.auth.isLoading = true

      ProfileApi.sendCode(this.phone)
        .then(response => {
          this.auth.isSmsSent = true
        })
        .finally(() => {
          this.auth.isLoading = false
        })
    },
    checkCode() {
      ProfileApi.checkCode(this.phone, this.code).then(response => {
        console.log(response)
        const { token } = response.data

        localStorage.setItem('token', token)
        api.defaults.headers.common['Authorization'] = token

        this.resetAuth()
      })
    },

    resetAuth() {
      this.auth = {
        phone: null,
        code: null,
        isLoading: false,
        isSmsSent: false,
      }
    },
  },
})
