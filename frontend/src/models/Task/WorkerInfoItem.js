export default class WorkerInfoItem {
  id
  fullName
  phone
  rating

  constructor(data = {}) {
    this.id = data.id
    this.fullName = data.fullName
    this.phone = data.phone
    this.rating = data.rating
  }
}
