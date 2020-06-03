<template>
  <div class="actTable">
    <el-table
      :data='actList'
      style='width:100%'
      size="small"
      max-height="700"
      :default-sort="{prop: 'time'}">
      <el-table-column type='expand'>
        <template slot-scope='props'>
          <el-form label-position='left' label-width="100px">
            <el-form-item label='活动ID'>{{props.row.id}}</el-form-item>
            <el-form-item label='活动名称'>{{props.row.name}}</el-form-item>
            <el-form-item label='活动主题'>{{props.row.theme}}</el-form-item>
            <el-form-item label='活动地点'>{{props.row.location}}</el-form-item>
            <el-form-item label='活动时间'>{{props.row.time}}</el-form-item>
            <el-form-item label='报名截止时间'>{{props.row.deadline}}</el-form-item>
            <el-form-item label='活动属性'>{{props.row.theme}}</el-form-item>
          </el-form>
        </template>
      </el-table-column>
      <el-table-column label='活动名称' prop='name'></el-table-column>
      <el-table-column label='类别' prop='type' :formatter='formatter'></el-table-column>
      <el-table-column label='地点' prop='location'></el-table-column>
      <el-table-column label='活动时间' prop='time' sortable></el-table-column>
      <el-table-column>
        <template slot-scope="props">
          <el-button @click="viewActivity(props.row)">查看活动</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>
<script>
import {get_all_activities, get_activity, get_signed_up_activities, get_joined_activities} from '../api/api.js'
export default {
  data () {
    return {
      actList: []
    }
  },
  props: ['listtype'],
  mounted: function () {
    this.loadAct(this.listtype)
  },
  methods: {
    viewActivity (row) {
      this.$router.push({name: 'activity', params: {'act': row}})
    },
    loadAct (type) {
      if (type === 'all') {
        get_all_activities({})
          .then(response => {
            console.log(response.data.data)
            let actid
            for (actid in response.data.data) {
              this.getAct(response.data.data[actid])
            }
          })
      } else if (type === 'signup') {
        get_signed_up_activities({
          userid: this.$cookies.get('userid')
        })
          .then(response => {
            console.log(response.data.data)
            let actid
            for (actid in response.data.data) {
              this.getAct(response.data.data[actid])
            }
          })
      } else if (type === 'join') {
        get_joined_activities({
          userid: this.$cookies.get('userid')
        })
          .then(response => {
            console.log(response.data.data)
            let actid
            for (actid in response.data.data) {
              this.getAct(response.data.data[actid])
            }
          })
      }
    },
    getAct (actid) {
      get_activity({
        id: actid
      })
        .then(response => {
          console.log(response.data)
          let act = response.data
          act.id = actid
          this.actList.push(act)
        })
    },
    formatter(row, column) {
      switch(row.type) {
        case 1: return "运动"
        case 2: return "学术"
        case 3: return "娱乐"
        case 4: return "吃喝"
        case 5: return "其他"
        default: return "无"
      }
    }
  }
}
</script>
<style scoped>
  .actTable{
    border:1px solid rgb(211, 208, 208); 
    border-radius: 2px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  }
</style>
