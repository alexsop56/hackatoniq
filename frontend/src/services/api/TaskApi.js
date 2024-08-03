import { api } from 'src/boot/axios'
import TaskListItem from 'src/models/Task/TaskListItem'
import WorkerInfoItem from 'src/models/Task/WorkerInfoItem'

export default class TaskApi {
  // TODO
  static index() {
    return new Promise(resolve => {
      const result = {
        data: {
          items: [
            new TaskListItem({
              id: 1,
              startDate: '08:00',
              startTime: '2024.01.01',
              address: 'г. Город, ул. Улица, д, 100',
              price: 100,
              views: 13,
              workersCount: 10,
              workersRequiredCount: 15,
              workers: [
                new WorkerInfoItem({
                  id: 1,
                  fullName: 'Зубенко Михаил Петрович',
                  phone: '+7 (912) 355 12-31',
                  rating: 1.5,
                }),
                new WorkerInfoItem({
                  id: 2,
                  fullName: 'Зубенко Михаил Петрович',
                  phone: '+7 (912) 355 12-32',
                  rating: 4.3,
                }),
                new WorkerInfoItem({
                  id: 3,
                  fullName: 'Зубенко Михаил Петрович',
                  phone: '+7 (912) 355 12-33',
                  rating: 3.8,
                }),
              ],
            }),
            new TaskListItem({
              id: 2,
              startDate: '08:00',
              startTime: '2024.01.02',
              address: 'г. Город, ул. Улица, д, 101',
              price: 10000,
              views: 13,
              workersCount: 3,
              workersRequiredCount: 5,
              workers: [
                new WorkerInfoItem({
                  id: 1,
                  fullName: 'Зубенко Михаил Петрович',
                  phone: '+7 (912) 355 12-31',
                  rating: 1.5,
                }),
                new WorkerInfoItem({
                  id: 2,
                  fullName: 'Зубенко Михаил Петрович',
                  phone: '+7 (912) 355 12-32',
                  rating: 4.3,
                }),
                new WorkerInfoItem({
                  id: 3,
                  fullName: 'Зубенко Михаил Петрович',
                  phone: '+7 (912) 355 12-33',
                  rating: 3.8,
                }),
              ],
            }),
          ],
          total: 1,
        },
      }

      setTimeout(() => resolve(result), 1000)
    })

    return api.get('tasks')
  }
}
