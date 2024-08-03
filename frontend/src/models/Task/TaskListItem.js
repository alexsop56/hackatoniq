export default class TaskListItem {
  id
  startDate
  startTime
  address
  price
  workersCount
  workersRequiredCount
  views
  workers

  constructor(data = {}) {
    this.id = data.id
    this.startDate = data.startDate
    this.startTime = data.startTime
    this.address = data.address
    this.price = data.price
    this.workersCount = data.workersCount
    this.workersRequiredCount = data.workersRequiredCount
    this.workers = data.workers
    this.views = data.views
  }
}
