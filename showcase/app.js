export const SHOWCASES = [
  {
    id: 'material-to-work',
    number: '案例 01',
    title: '从一条真实学习记录创建作品',
    problem: '解决素材、选题和稿件彼此割裂，创作时反复寻找上下文的问题。',
    input: '素材：第一次独立定位 Python 项目启动错误；状态：用户已亲测；待补：复现步骤截图。',
    result: '1 个作品 · 2 种内容形式 · 1 份定位快照',
    detail: '从素材创建作品，同时选择“图文”和“录屏教程”；作品保存创建时的定位快照，后续修改账号定位不会改写旧作品。',
    steps: ['关联有来源状态的素材', '创建选题与作品记录', '保存形式和定位快照'],
    guardrail: '尚未完成的截图会保留为“待补”，不会被写成已经亲测的结果。',
  },
  {
    id: 'version-production',
    number: '案例 02',
    title: '把初稿推进到可执行的制作清单',
    problem: '解决 AI 改稿覆盖旧内容、稿件与实际制作任务脱节的问题。',
    input: '作品：Python 报错排查；形式：6 页图文 + 180 秒录屏教程；每周创作预算：6 小时。',
    result: '版本留存 · Markdown / CSV 导出 · 按顺序排期',
    detail: '每次生成或人工修改都创建新版本；确认稿可生成标题、封面文字、发布介绍和 SOP，任务按前后依赖与每周时间预算安排。',
    steps: ['校验图文页数与视频时长', '保存新稿而不覆盖旧版本', '生成并安排制作任务'],
    guardrail: '生成失败会保留已有稿件；排不进本周预算的任务顺延，不跳过尚未完成的前置步骤。',
  },
  {
    id: 'publish-review',
    number: '案例 03',
    title: '让发布数据回到下一轮选题',
    problem: '解决只记录播放量、缺少观察口径，导致不同内容无法合理比较的问题。',
    input: '发布：B站与小红书；记录发布日期、观察天数、已有指标、评论反馈和创作者感受。',
    result: '按平台、形式与观察天数分组复盘',
    detail: '系统保留缺失指标为空，只在同口径分组内归纳；被明确采纳的新问题会回到选题收藏，形成下一轮创作输入。',
    steps: ['登记平台与观察天数', '分组整理数据和反馈', '将采纳问题写回选题池'],
    guardrail: '小样本只形成待验证假设；资料不足时明确说明，不承诺浏览量、涨粉或爆款结果。',
  },
]

export function selectShowcase(id) {
  return SHOWCASES.find((item) => item.id === id) ?? SHOWCASES[0]
}

function renderShowcase(id) {
  const item = selectShowcase(id)
  const fields = {
    '[data-demo-number]': item.number,
    '[data-demo-title]': item.title,
    '[data-demo-problem]': item.problem,
    '[data-demo-input]': item.input,
    '[data-demo-result]': item.result,
    '[data-demo-detail]': item.detail,
    '[data-demo-guardrail]': item.guardrail,
  }

  Object.entries(fields).forEach(([selector, value]) => {
    const node = document.querySelector(selector)
    if (node) node.textContent = value
  })

  const steps = document.querySelector('[data-demo-steps]')
  if (steps) {
    steps.replaceChildren(...item.steps.map((text) => {
      const row = document.createElement('li')
      row.textContent = text
      return row
    }))
  }

  document.querySelectorAll('[data-demo-id]').forEach((button) => {
    button.setAttribute('aria-pressed', String(button.dataset.demoId === item.id))
  })
}

if (typeof document !== 'undefined') {
  document.querySelectorAll('[data-demo-id]').forEach((button) => {
    button.addEventListener('click', () => renderShowcase(button.dataset.demoId))
  })
  renderShowcase(SHOWCASES[0].id)
}

