import request from '@/utils/request'

// 获取学生信息
export function getStudent (token) {
  return request({
    url: '/jwt/student',
    method: 'get',
    params: { token }
  })
}
