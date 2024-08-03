<template>
  <q-item class="q-ma-sm bg-white br-10">
    <q-expansion-item header-class="q-pa-none" class="full-width">
      <template v-slot:header>
        <q-item-section>Скелетон</q-item-section>
        <q-item-section>Скелетон</q-item-section>
      </template>

      <div class="row items-center q-mt-sm">content</div>
    </q-expansion-item>
  </q-item>
</template>

<script>
export default {
  name: 'TaskListItemSkeleton',
}
</script>
