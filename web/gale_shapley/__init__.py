import collections


class GaleShapley(object):
    def __init__(self, preferred_rankings_mentor, preferred_rankings_mentee):
        # The mentee that the mentor prefer\
        self.preferred_rankings_mentor = preferred_rankings_mentor
        # {
        #     'ryan': ['lizzy', 'sarah', 'zoey', 'daniella'],
        #     'josh': ['sarah', 'lizzy', 'daniella', 'zoey'],
        #     'blake': ['sarah', 'daniella', 'zoey', 'lizzy'],
        #     'connor': ['lizzy', 'sarah', 'zoey', 'daniella']
        # }

        # The mentor that the mentee prefer
        self.preferred_rankings_mentee = preferred_rankings_mentee
        # {
        #     'lizzy': ['ryan', 'blake', 'josh', 'connor'],
        #     'sarah': ['ryan', 'blake', 'connor', 'josh'],
        #     'zoey': ['connor', 'josh', 'ryan', 'blake'],
        #     'daniella': ['ryan', 'josh', 'connor', 'blake']
        # }

        # Keep track of the people that "may" end up together
        self.tentative_engagements = []

        # mentor who still need to propose and get accepted successfully
        self.free_mentor = []
        self._init_free_mentor()


    def _init_free_mentor(self):
        '''Initialize the arrays of mentee and mentor to represent
            that they're all initially free and not engaged'''
        for mentor in self.preferred_rankings_mentor.keys():
            self.free_mentor.append(mentor)


    def _begin_matching(self, mentor):
        '''Find the first free mentee available to a mentor at
            any given time'''

        print("DEALING WITH %s" % (mentor))
        for mentee in self.preferred_rankings_mentor[mentor]:

            # Boolean for whether mentee is taken or not
            taken_match = [pair for pair in self.tentative_engagements if mentee in pair]

            if (len(taken_match) == 0):
                # tentatively engage the mentor and mentee
                self.tentative_engagements.append([mentor, mentee])
                self.free_mentor.remove(mentor)
                print(
                    '%s is no longer a free mentor and is now tentatively matched to %s' % (
                    mentor, mentee))
                break

            elif (len(taken_match) > 0):
                print('%s is taken already..' % (mentee))

                # Check ranking of the current dude and the ranking of the 'to-be' dude
                current_mentor_rank = self.preferred_rankings_mentee[mentee].index(taken_match[0][0])
                potential_mentor_rank = self.preferred_rankings_mentee[mentee].index(mentor)

                if (current_mentor_rank < potential_mentor_rank):
                    print('Mentor is satisfied with %s..' % (taken_match[0][0]))
                else:
                    print('%s is better than %s' % (mentor, taken_match[0][0]))
                    print('Making %s free again.. and tentatively matching %s and %s' % (
                    taken_match[0][0], mentor, mentee))

                    # The new mentor is no longer free
                    self.free_mentor.remove(mentor)

                    # The old mentor is now free
                    self.free_mentor.append(taken_match[0][0])

                    # Update the match of the mentee (tentatively)
                    taken_match[0][0] = mentor
                    break  # TODO review this break


    def stable_matching(self):
        '''Matching algorithm until stable match terminates'''
        while (len(self.free_mentor) > 0):
            for mentor in self.free_mentor:
                self._begin_matching(mentor)
        return self.tentative_engagements


def find_stable_match(preferred_rankings_mentor, preferred_rankings_mentee):
    matcher = GaleShapley(preferred_rankings_mentor, preferred_rankings_mentee)
    return matcher.stable_matching()
