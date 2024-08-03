import { api } from 'src/boot/axios'
import ProjectListItem from 'src/models/Project/ProjectListItem'
import TaskInfoItem from 'src/models/Project/TaskInfoItem'

export default class ProjectApi {
  // TODO
  static index() {
    return new Promise(resolve => {
      const result = {
        data: {
          items: [
            new ProjectListItem({
              id: 1,
              title: 'Название',
              address: 'какой то адрес',
              tasksCount: 10,
              workersCount: 5,
              workersRequiredCount: 13,
              address: 'Улица пушкина, дом колотушкина',
              attentionCount: 2,
              todoCount: 19,
              tasks: [
                new TaskInfoItem({
                  id: 1,
                  workTypeTitle: 'Укладка плитки',
                  workersCount: 1,
                  workersRequiredCount: 10,
                }),
              ],
            }),
          ],
          total: 1,
        },
      }

      setTimeout(() => resolve(result), 1000)
    })

    return api.get('projects')
  }
}
