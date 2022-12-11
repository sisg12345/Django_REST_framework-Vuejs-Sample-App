<template>
  <div class="alert alert-danger alert-dismissible fade show" role="alert" v-if="errorMessage !== null">
    {{ errorMessage }}
    <button type="button" class="close" data-dismiss="alert" aria-label="Close" @click="closeMessage">
      <span aria-hidden="true">&times;</span>
    </button>
  </div>
</template>
<script>
export default {
  name: 'ErrorMessageArea',
  props: {
    errorMessage: {
      type: String,
      require: true
    }
  },
  setup(props, context) {
    // エラーメッセージ閉じる
    const closeMessage = () => {
      // エラーメッセージを閉じる処理呼び出し
      context.emit('closeMessage')
    }

    return {
      closeMessage
    }
  }
}
</script>