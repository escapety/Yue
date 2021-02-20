<template>
  <el-form :model="user" :rules="rules" ref="newuser">
    <el-form-item label="用户名" prop="name">
      <el-input v-model="user.name" clearable></el-input>
    </el-form-item>
    <el-form-item label="密码" prop="password">
      <el-input v-model="user.password" show-password clearable></el-input>
    </el-form-item>
    <el-form-item label="确认密码" prop="checkpassword">
      <el-input v-model="user.checkpassword" show-password clearable></el-input>
    </el-form-item>
    <el-alert title="注册失败" type="error" center :closable="false" v-show="showerror"></el-alert>
    <el-form-item>
      <el-button type="primary" @click="register">注册</el-button>
    </el-form-item>
  </el-form>
</template>
<script>
import {new_user} from '../api/api.js'
export default {
  data () {
    var checkPassword = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请重复密码'))
      } else if (value !== this.user.password) {
        callback(new Error('两次输入密码不一致'))
      } else {
        callback()
      }
    }
    return {
      user: {
        name: '',
        password: '',
        checkpassword: ''
      },
      showerror: false,
      rules: {
        name: [
          { required: true, message: '请输入用户名', triggle: 'blur' },
          { min: 5, message: '长度至少为5个字符', triggle: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', triggle: 'blur' }
        ],
        checkpassword: [
          { required: true, validator: checkPassword, triggle: 'blur' }
        ]
      }
    }
  },
  methods: {
    register () {
      this.$refs['newuser'].validate((valid) => {
        if (valid) {
          new_user({
            name: this.user.name,
            password: this.user.password
          })
            .then(response => {
              console.log(response.data)
              this.$cookies.set('userid', response.data.user_id)
              this.$router.push('main')
            })
            .catch(error => {
              this.showerror = true
              console.log(error)
            })
        }
        this.$refs['newuser'].resetFields()
      })
    }
  }
}
</script>
