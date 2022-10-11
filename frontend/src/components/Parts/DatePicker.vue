<template>
  <div id="datepicker">
    <Datepicker :bootstrap-styling="true" :format="dateFormat" locale="jp" cancel-text="キャンセル" select-text="OK" v-model="dateTime"></Datepicker>
  </div>
</template>
<script>
import { ref } from 'vue'
import Datepicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'

export default {
  name: 'DatePicker',
  components: {
    Datepicker
  },
  setup() {
    // 日付
    const dateTime = ref(null)
    // 日付フォーマット: yyyy/MM/dd HH:mm
    const dateFormat = ref('yyyy/MM/dd HH:mm')

    return {
      dateTime,
      dateFormat
    }
  }
}
</script>