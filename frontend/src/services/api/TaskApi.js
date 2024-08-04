import { api } from 'src/boot/axios'
import TaskListItem from 'src/models/Task/TaskListItem'
import WorkerInfoItem from 'src/models/Task/WorkerInfoItem'

const TASKS_LIST = [
  new TaskListItem({
    id: 1,
    startDate: '08:00',
    startTime: '01.01.2024',
    title: 'Название 1',
    workTypeTitle: 'Укладка плитки',
    price: 100,
    totalPrice: 1000,
    isFinished: true,
    views: 13,
    workersCount: 10,
    workersRequiredCount: 15,
    workers: [
      new WorkerInfoItem({
        id: 1,
        fullName: 'Зубенко Михаил Петрович',
        phone: '+7 (912) 355 12-31',
        fact: 43,
        plan: 1000,
      }),
      new WorkerInfoItem({
        id: 2,
        fullName: 'Зубенко Михаил Петрович',
        phone: '+7 (912) 355 12-32',
        fact: 41,
        plan: 1000,
      }),
      new WorkerInfoItem({
        id: 3,
        fullName: 'Зубенко Михаил Петрович',
        phone: '+7 (912) 355 12-33',
        fact: 99,
        plan: 1000,
      }),
    ],
  }),
  new TaskListItem({
    id: 2,
    startDate: '08:00',
    startTime: '02.01.2024',
    title: 'Название 2',
    price: 10000,
    totalPrice: 1000,
    isFinished: false,
    workTypeTitle: 'Укладка плитки',
    views: 13,
    workersCount: 3,
    workersRequiredCount: 5,
    workers: [
      new WorkerInfoItem({
        id: 1,
        fullName: 'Зубенко Михаил Петрович',
        phone: '+7 (912) 355 12-31',
        reliability: 43,
        plan: 1000,
      }),
      new WorkerInfoItem({
        id: 2,
        fullName: 'Зубенко Михаил Петрович',
        phone: '+7 (912) 355 12-32',
        reliability: 41,
        plan: 1000,
      }),
      new WorkerInfoItem({
        id: 3,
        fullName: 'Зубенко Михаил Петрович',
        phone: '+7 (912) 355 12-33',
        reliability: 99,
        plan: 1000,
      }),
    ],
  }),
]

export default class TaskApi {
  // TODO
  static index() {
    return new Promise(resolve => {
      const result = {
        data: {
          items: TASKS_LIST,
          total: TASKS_LIST.length,
        },
      }

      setTimeout(() => resolve(result), 1000)
    })

    return api.get('tasks')
  }

  static store(data) {
    return new Promise(resolve => {
      const result = {
        data: {
          items: [new TaskListItem(data)],
        },
      }

      setTimeout(() => resolve(result), 1000)
    })

    return api.post('tasks')
  }
}
