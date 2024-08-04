import { api } from 'src/boot/axios'
import ProjectListItem from 'src/models/Project/ProjectListItem'
import TaskInfoItem from 'src/models/Project/TaskInfoItem'

const PROJECTS = [
  new ProjectListItem({
    id: 1,
    title: 'Название',
    address: 'какой то адрес',
    tasksCount: 10,
    workersCount: 5,
    workersRequiredCount: 13,
    address: 'Улица пушкина',
    attentionCount: 2,
    todoCount: 19,
    budget: 100000,
    spentBudget: 1000,
    tasks: [
      // new TaskInfoItem({
      //   id: 1,
      //   workTypeTitle: 'Укладка плитки',
      //   workersCount: 1,
      //   workersRequiredCount: 10,
      // }),
      // new TaskInfoItem({
      //   id: 1,
      //   workTypeTitle: 'Укладка плитки',
      //   workersCount: 5,
      //   workersRequiredCount: 10,
      // }),
      // new TaskInfoItem({
      //   id: 1,
      //   workTypeTitle: 'Укладка плитки',
      //   workersCount: 10,
      //   workersRequiredCount: 10,
      // }),
    ],
  }),
]
export default class ProjectApi {
  // TODO
  static index() {
    return new Promise(resolve => {
      const result = {
        data: {
          items: PROJECTS,
          total: PROJECTS.length,
        },
      }

      setTimeout(() => resolve(result), 1000)
    })

    return api.get('projects')
  }

  static show(projectId) {
    return new Promise(resolve => {
      const result = PROJECTS.find(v => v.id == projectId)

      setTimeout(() => resolve(result), 1000)
    })

    return api.get(`projects/${projectId}`)
  }

  static store(data) {
    return new Promise(resolve => {
      const result = {
        data: {
          items: [new ProjectListItem(data)],
        },
      }

      setTimeout(() => resolve(result), 1000)
    })

    return api.post(`projects`)
  }
}
