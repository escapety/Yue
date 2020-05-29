<template>
  <el-table :data='actList' style='width:100%' border>
    <!-- <el-table-column type='expand'>
      <template slot-scope='props'>
        <el-form label-position='left' label-width="100px">
          <el-form-item label='活动ID'>{{props.row.id}}</el-form-item>
          <el-form-item label='活动名称'>{{props.row.name}}</el-form-item>
          <el-form-item label='活动主题'>{{props.row.theme}}</el-form-item>
          <el-form-item label='活动地点'>{{props.row.location}}</el-form-item>
          <el-form-item label='活动时间'>{{props.row.time}}</el-form-item>
          <el-form-item label='报名截止时间'>{{props.row.deadline}}</el-form-item>
          <el-form-item label='活动属性'>{{props.row.theme}}</el-form-item>
          <el-form-item>
            <el-button @click="joinAct">加入活动</el-button>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column> -->
    <el-table-column label='活动主题' prop='theme'></el-table-column>
    <el-table-column label='活动时间' prop='time'></el-table-column>
    <el-table-column label='地点' prop='location'></el-table-column>
    <el-table-column label=''>
      <template slot-scope="scope">
        <el-button @click="viewActivity(scope.row)" type="text">查看活动</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>
<script>
export default {
  data () {
    return {
      actList: []
    }
  },
  props: ['listtype'],
  created: function () {
    this.loadAct()
  },
  methods: {
    viewActivity (row) {
      this.$router.push({path: '/Activity', query: {'id': row.id}})
    },
    loadAct () {
      let _this = this
      if (this.listtype === 'all') {
        this.$axios({
          method: 'get',
          url: '/BackEnd/get_all_activities/'
        })
          .then(function (response) {
            console.log(response.data.data)
            let actid
            for (actid in response.data.data) {
              _this.getAct(response.data.data[actid])
            }
          })
      } else if (this.listtype === 'signup') {
        this.$axios({
          method: 'get',
          url: '/BackEnd/get_signed_up_activities/',
          params: {
            userid: this.$cookies.get('userid')
          }
        })
          .then(function (response) {
            console.log(response.data.data)
            let actid
            for (actid in response.data.data) {
              _this.getAct(response.data.data[actid])
            }
          })
      } else if (this.listtype === 'join') {
        this.$axios({
          method: 'get',
          url: '/BackEnd/get_joined_activities/',
          params: {
            userid: this.$cookies.get('userid')
          }
        })
          .then(function (response) {
            console.log(response.data.data)
            let actid
            for (actid in response.data.data) {
              _this.getAct(response.data.data[actid])
            }
          })
      }
    },
    getAct (actid) {
      let _this = this
      this.$axios({
        method: 'get',
        url: '/BackEnd/get_activity/',
        params: {
          id: actid
        }
      })
        .then(function (response) {
          console.log(response.data)
          let act = response.data
          act.id = actid
          _this.actList.push(act)
        })
    }
  }
}
</script>
<style>

</style>
