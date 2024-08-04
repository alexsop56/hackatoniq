import { api } from 'src/boot/axios'

const PROFILE = {
  id: 1,
  phone: '+7 (912) 355 12-34',
  balance: 10000,
  spentBalance: 1000,
}

export default class AuthApi {
  static sendCode(email) {
    return api.post('auth/send-code', { email })
  }

  static checkCode(email, code, ref) {
    return api.get('auth/check-code', { params: { email, code, ref } })
  }

  static getMe() {
    return new Promise(resolve => {
      const result = {
        data: PROFILE,
      }

      setTimeout(() => resolve(result), 1000)
    })

    return api.get('projects')
  }
}
