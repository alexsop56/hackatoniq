<template>
  <q-layout view="hHh lpr fFf">
    <q-header>
      <q-toolbar>
        <q-space />

        <q-icon name="engineering" size="30px" />
      </q-toolbar>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer class="shadow-2">
      <q-tabs v-model="tab" indicator-color="transparent" active-color="primary" class="bg-white text-secondary">
        <q-route-tab
          v-for="routeButton in routeButtons"
          :to="routeButton.to"
          :name="routeButton.name"
          :key="routeButton.name"
          :label="routeButton.label"
          :icon="routeButton.icon"
          no-caps
        />
      </q-tabs>
    </q-footer>
  </q-layout>
</template>

<script>
export default {
  name: 'MainLayout',
  data() {
    return {
      tab: 'projects',

      routeButtons: [
        {
          label: 'Проекты',
          name: 'projects',
          to: { path: '/projects' },
          icon: 'format_list_bulleted',
        },
        {
          label: 'Вкладка 2',
          name: 'name2',
          to: { path: '/name2' },
          icon: 'work',
        },
        {
          label: 'Вкладка 3',
          name: 'name3',
          to: { path: '/name3' },
          icon: 'pin_drop',
        },
        {
          label: 'Вкладка 4',
          name: 'name4',
          to: { path: '/name4' },
          icon: 'person',
        },
      ],
    }
  },
}
</script>
