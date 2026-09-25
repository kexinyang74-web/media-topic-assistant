import assert from 'node:assert/strict'
import test from 'node:test'
import { SHOWCASES, selectShowcase } from '../showcase/app.js'

test('contains exactly three showcase flows', () => {
  assert.equal(SHOWCASES.length, 3)
})

test('selectShowcase returns the requested flow', () => {
  assert.equal(selectShowcase('version-production').id, 'version-production')
})

test('selectShowcase falls back to the first flow', () => {
  assert.equal(selectShowcase('missing').id, SHOWCASES[0].id)
  assert.equal(selectShowcase().id, SHOWCASES[0].id)
})

