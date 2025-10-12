#[allow(dead_code)]
struct Solution;

use std::collections::{HashMap, HashSet};

impl Solution {
    #[allow(dead_code)]
    #[allow(clippy::needless_pass_by_value)]
    pub fn find_all_recipes(
        recipes: Vec<String>,
        ingredients: Vec<Vec<String>>,
        supplies: Vec<String>,
    ) -> Vec<String> {
        let unique_supplies = supplies
            .iter()
            .map(String::as_str)
            .collect::<HashSet<&str>>();
        let mut graph: HashMap<&str, Vec<&str>> = HashMap::new();

        for (i, recipe) in recipes.iter().map(String::as_str).enumerate() {
            graph.insert(recipe, ingredients[i].iter().map(String::as_str).collect());
        }

        let mut result = Vec::new();
        let mut visited: HashMap<String, bool> = HashMap::new();

        for recipe in &recipes {
            if Self::dfs(recipe, &graph, &unique_supplies, &mut visited) {
                result.push(recipe.clone());
            }
        }
        result
    }

    fn dfs(
        recipe: &str,
        graph: &HashMap<&str, Vec<&str>>,
        supplies: &HashSet<&str>,
        visited: &mut HashMap<String, bool>,
    ) -> bool {
        if visited.contains_key(recipe) {
            return *visited.get(recipe).unwrap();
        }

        visited.insert(recipe.to_string(), false);

        for next in graph.get(recipe).unwrap() {
            if supplies.contains(next) {
                continue;
            }

            if graph.contains_key(next) {
                if !Self::dfs(next, graph, supplies, visited) {
                    return false;
                }
                continue;
            }

            return false;
        }

        visited.insert(recipe.to_string(), true);

        true
    }
}
