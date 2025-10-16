#[allow(dead_code)]
struct Solution;

use std::collections::VecDeque;

impl Solution {
    #[allow(dead_code, clippy::needless_pass_by_value)]
    pub fn find_order(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> Vec<i32> {
        let mut indegrees = vec![0; num_courses.try_into().unwrap()];
        let mut next_courses: Vec<Vec<i32>> = vec![vec![]; num_courses.try_into().unwrap()];

        for course_prerequisite in prerequisites.as_slice() {
            let course = course_prerequisite[0];
            let prerequisite = usize::try_from(course_prerequisite[1]).unwrap();
            next_courses[prerequisite].push(course);
            indegrees[usize::try_from(course).unwrap()] += 1;
        }

        let mut queue = VecDeque::new();

        for course in indegrees
            .iter()
            .enumerate()
            .filter(|(_, c)| **c == 0)
            .map(|(c, _)| c)
        {
            queue.push_back(course);
        }

        let mut res = Vec::new();

        while let Some(course) = queue.pop_front() {
            res.push(course.try_into().unwrap());
            for next_course in next_courses[course].as_slice() {
                let next_course_usize = usize::try_from(*next_course).unwrap();
                indegrees[next_course_usize] -= 1;

                if indegrees[next_course_usize] == 0 {
                    queue.push_back(next_course_usize);
                }
            }
        }

        if num_courses > res.len().try_into().unwrap() {
            return vec![];
        }

        res
    }
}
