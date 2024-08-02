const routes = [
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
    meta: {
      isAuthRequired: false,
    },
  },
]

export default routes
