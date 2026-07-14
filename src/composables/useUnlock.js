/**
 * Time-based unlock logic.
 *
 * Every unlockable item has a `date` (or `unlockDate`) field in ISO format
 * ("YYYY-MM-DD"). An item is unlocked the moment the visitor's local date
 * reaches that date. To change when something unlocks, just edit the date
 * in the corresponding JSON file under src/data/ — no code changes needed.
 */

export function isUnlocked(isoDate) {
  if (!isoDate) return false
  const today = new Date()
  today.setHours(0, 0, 0, 0)
  const target = new Date(isoDate + 'T00:00:00')
  return target.getTime() <= today.getTime()
}

export function daysUntil(isoDate) {
  const today = new Date()
  today.setHours(0, 0, 0, 0)
  const target = new Date(isoDate + 'T00:00:00')
  const diffMs = target.getTime() - today.getTime()
  return Math.ceil(diffMs / (1000 * 60 * 60 * 24))
}

export function formatDate(isoDate) {
  const d = new Date(isoDate + 'T00:00:00')
  return d.toLocaleDateString('it-IT', { day: 'numeric', month: 'long', year: 'numeric' })
}

/** Decorate a list of items (each with a `date` field) with unlock state. */
export function withUnlockState(items, dateField = 'date') {
  return items.map((item) => ({
    ...item,
    unlocked: isUnlocked(item[dateField]),
    daysUntil: daysUntil(item[dateField]),
  }))
}
