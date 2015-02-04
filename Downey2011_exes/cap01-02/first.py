#!/usr/bin/python
# vim: set fileencoding=utf8 :

"""
# UFRJ - PPGI
# MAB719
# Cristiano Gurgel de Castro <crisgc1@gmail.com>

ThinkStats: Exercício 1.3
"""

import survey
import stats

table = survey.Pregnancies()
table.ReadRecords()

# Calculates the number of live births
n_live_births = len([1 for record in table.records if record.outcome == 1])

# Partition the record in two groups of babies (1st pregs and non-1st pregs)
first_live_births = [record for record in table.records if record.outcome == 1
    and record.birthord == 1]
non_first_live_births = [record for record in table.records if record.outcome ==
        1 and record.birthord != 1]

# Compute the Mean preg time in weeks for 1st pregs and non-1st pregs

weeks_first_preg = [record.prglength for record in first_live_births]
weeks_non_first_preg = [record.prglength for record in non_first_live_births]
weeks_all = [record.prglength for record in table.records if record.outcome ==
        1]

mean_weeks_first = stats.mean(weeks_first_preg)
mean_weeks_non_first = stats.mean(weeks_non_first_preg)
diff_weeks = mean_weeks_first - mean_weeks_non_first 

if __name__ == '__main__':
    print 'Number of pregnancies' , len(table.records)

    # Expected: 9148 
    print 'Live births %d' % n_live_births
    print 'Live births (1st pregnancies) %d' % len(first_live_births)

    print 'Mean weeks for first pregs %.3f' % mean_weeks_first
    print 'Mean weeks for non-first pregs %.3f' % mean_weeks_non_first

    print 'Difference (in hours) %.3f' % (diff_weeks * 24 * 7)

