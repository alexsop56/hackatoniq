export default class Task {
  id
  period
  price
  workTypeTitle
  workersRequiredCount

  constructor(data = {}) {
    this.id = data.id
    this.period = data.period
    this.price = data.price
    this.workTypeTitle = data.workTypeTitle
    this.workersRequiredCount = data.workersRequiredCount
  }
}
