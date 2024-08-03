const routes = [
  {
    path: '/auth',
    component: () => import('src/pages/AuthPage.vue'),
    meta: {
      isAuthRequired: false,
    },
  },
  {
    path: '/',
    redirect: 'projects',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: 'projects',
        component: () => import('src/pages/ProjectsPage.vue'),
        meta: {
          title: 'Проекты',
          isAuthRequired: false, // TODO: switch on
        },
      },
      {
        path: 'projects/:id',
        component: () => import('src/pages/ProjectPage.vue'),
        meta: {
          title: 'Проект',
          isAuthRequired: false, // TODO: switch on
        },
      },
    ],
  },
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
    meta: {
      isAuthRequired: false,
    },
  },
]

export default routes
