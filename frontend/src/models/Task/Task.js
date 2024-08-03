export default class Task {
  id
  title
  tasksCount
  workersCount
  workersRequiredCount
  address
  attentionCount
  todoCount
  views
  tasks

  constructor(data = {}) {
    this.id = data.id
  }
}
