import { api } from 'src/boot/axios'

export default class AuthApi {
  static sendCode(email) {
    return api.post('auth/send-code', { email })
  }

  static checkCode(email, code, ref) {
    return api.get('auth/check-code', { params: { email, code, ref } })
  }
}
