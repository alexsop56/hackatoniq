import { api } from 'src/boot/axios'

const PROFILE = {
  id: 1,
  phone: '+7 (912) 355 12-34',
  balance: 10000,
  spentBalance: 1000,
}

export default class ProfileApi {
  static sendCode(phone) {
    return api.post('projects', { phone })
  }

  static checkCode(phone, code) {
    return { data: { token: 'sometoken' } }
    return api.get('auth/check-code', { params: { phone, code } })
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
