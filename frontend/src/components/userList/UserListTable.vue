<template>
  <div id="userListTable">
    <!-- 複数件データ削除用ボタン -->
    <div class="container mb-1">
      <div class="row text-right">
          <div class="col-12">
            <DeleteButton @click="deleteMultiUserInfo"></DeleteButton>
          </div>
      </div>
    </div>
    <!-- テーブル -->
    <TableLite
      :has-checkbox="true"
      :is-loading="table.isLoading"
      :is-re-search="table.isReSearch"
      :columns="table.columns"
      :rows="table.rows"
      :rowClasses="table.rowClasses"
      :total="table.totalRecordCount"
      :sortable="table.sortable"
      :messages="table.messages"
      @do-search="doSearch"
      @is-finished="tableLoadingFinish"
      @return-checked-rows="updateCheckedRows"
      @row-clicked="rowClicked"
    ></TableLite>
    <br>
  </div>
</template>

<script>
import { reactive } from "vue"
import TableLite from 'vue3-table-lite'
import DeleteButton from '../Parts/DeleteButton.vue'


export default {
  name: "UserListTable",
  components: { TableLite, DeleteButton },
  emits: [ 'editUserInfo', 'deleteUserInfo', 'deleteMultiUserInfo' ],
  setup(props, context) {
    // Table config
    const table = reactive({
      isLoading: false,
      isReSearch: false,
      columns: [
        {
          label: "ID",
          field: "id",
          width: "5%",
          sortable: true,
          isKey: true,
        },
        {
          label: "ユーザー名",
          field: "user_name",
          width: "10%",
          sortable: true,
        },
        {
          label: "メールアドレス",
          field: "email",
          width: "10%",
          sortable: true,
        },
        {
          label: "ユーザータイプ",
          field: "user_type",
          width: "12%",
          sortable: true,
        },
        {
          label: "最終ログイン日付",
          field: "last_login",
          width: "10%",
          sortable: true,
        },
        {
          label: "",
          field: "btn",
          width: "5%",
          display: function (row) {
            return (
              '<button type="button" data-id="' +
              row.id +
              '" class="is-rows-el edit-btn btn btn-outline-primary">編集</button>'
              + '&nbsp;&nbsp;&nbsp;' + 
              '<button type="button" data-id="' +
              row.id +
              '" class="is-rows-el delete-btn btn btn-outline-danger">削除</button>'
            );
          },
        },
      ],
      rows: [],
      totalRecordCount: 0,
      sortable: {
        // order: "email",
        sort: "asc",
      },
      messages: {
        pagingInfo: "表示 {0}-{1} / {2}",
        pageSizeChangeLabel: "表示行数:",
        gotoPageLabel: "ページ移動:",
        noDataAvailable: "データなし",
      },
    })

    // 選択した複数行のキー
    var selectedRowsKey = []
     
    /**
     * Search Event
     */
    const doSearch = (offset, limit, tableData, order, sort) => {
      table.isLoading = true
      setTimeout(() => {
        table.isReSearch = offset == undefined ? true : false
        if (offset >= 10 || limit >= 20) {
          limit = 20
        }
        table.rows = tableData
        table.totalRecordCount = tableData.length
        table.sortable.order = order
        table.sortable.sort = sort
      }, 600)
    }

    /**
     * Loading finish event
     */
    const tableLoadingFinish = (elements) => {
      table.isLoading = false
      Array.prototype.forEach.call(elements, function (element) {
        // 編集する対象データ
        var editUserData = null

        // 編集ボタンクリック時のイベント探知処理
        if (element.classList.contains("edit-btn")) {
          element.addEventListener("click", function (event) {
            event.stopPropagation() // prevents further propagation of the current event in the capturing and bubbling phases.
            // 一覧データから編集する対象データを取得
            table.rows.forEach(value => {
              if (this.dataset.id == value.id) {
                editUserData = value
                return
              }
            })
            // 編集モーダル表示処理呼び出し
            if (editUserData !== null) {
              context.emit('editUserInfo', editUserData)
            }        
          })
        }
        // 削除ボタンクリック時のイベント探知処理
        if (element.classList.contains("delete-btn")) {
          element.addEventListener("click", function (event) {
            event.stopPropagation() // prevents further propagation of the current event in the capturing and bubbling phases.
            // 削除処理呼び出し
            context.emit('deleteUserInfo', this.dataset.id)
          })
        }
      })
    }

    /**
     * Row checked event
     */
    const updateCheckedRows = (rowsKey) => {
      selectedRowsKey = rowsKey
    }

    // First get data
    // doSearch(0, 10, "id", "asc")

    /**
     * Row clicked event
     */
    const rowClicked = (row) => {
      console.log("Row clicked!", row)
    }

    // ユーザーデータ複数件削除処理呼び出し
    const deleteMultiUserInfo = () => {
      context.emit('deleteMultiUserInfo', selectedRowsKey)
    } 

    return {
      table,
      doSearch,
      tableLoadingFinish,
      updateCheckedRows,
      rowClicked,
      deleteMultiUserInfo
    }
  }
}
</script>
<style scoped>
::v-deep(.vtl-table .vtl-thead .vtl-thead-th) {
  color: #fff;
  background-color: #FC466B;
  border-color: #FC466B;
}
</style>