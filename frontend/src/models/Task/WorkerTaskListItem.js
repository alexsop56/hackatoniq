export default class WorkerTaskListItem {
  id
  startDate
  startTime
  title
  price
  workTypeTitle
  workersCount
  workersRequiredCount

  constructor(data = {}) {
    this.id = data.id
    this.startDate = data.startDate
    this.startTime = data.startTime
    this.title = data.title
    this.price = data.price
    this.workTypeTitle = data.workTypeTitle
    this.workersCount = data.workersCount
    this.workersRequiredCount = data.workersRequiredCount
  }
}
