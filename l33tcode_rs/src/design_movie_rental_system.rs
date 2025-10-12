use std::collections::{BinaryHeap, HashMap};

#[allow(dead_code)]
struct MovieRentingSystem {
    all_stock: HashMap<i32, HashMap<i32, i32>>, // shop -> movie -> price
    rented: HashMap<i32, HashMap<i32, i32>>,    // shop -> movie -> price
    movie_index: HashMap<i32, Vec<(i32, i32)>>, // movie -> Vec<(shop, price)>
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
#[allow(dead_code)]
impl MovieRentingSystem {
    fn new(_n: i32, entries: Vec<Vec<i32>>) -> Self {
        let mut all_stock = HashMap::new();
        let rented = HashMap::new();
        let mut movie_index: HashMap<i32, Vec<(i32, i32)>> = HashMap::new();

        for entry in entries {
            let shop = entry.first().unwrap();
            let movie = entry.get(1).unwrap();
            let price = entry.get(2).unwrap();

            movie_index.entry(*movie).or_default().push((*shop, *price));

            all_stock
                .entry(*shop)
                .or_insert(HashMap::new())
                .insert(*movie, *price);
        }

        for (_, shops_and_prices) in &mut movie_index.iter_mut() {
            shops_and_prices.sort_by_key(|x| (x.1, x.0));
        }

        MovieRentingSystem {
            all_stock,
            rented,
            movie_index,
        }
    }

    fn search(&mut self, movie: i32) -> Vec<i32> {
        let mut res = Vec::new();

        for (shop, _) in self.movie_index.entry(movie).or_default() {
            if !self
                .rented
                .get(shop)
                .is_some_and(|inner| inner.contains_key(&movie))
            {
                if res.len() < 5 {
                    res.push(*shop);
                } else {
                    break;
                }
            }
        }

        res
    }

    fn rent(&mut self, shop: i32, movie: i32) {
        self.rented
            .entry(shop)
            .or_default()
            .entry(movie)
            .or_insert(*self.all_stock.get(&shop).unwrap().get(&movie).unwrap());
    }

    fn drop(&mut self, shop: i32, movie: i32) {
        self.rented.entry(shop).or_default().remove(&movie);
    }

    fn report(&self) -> Vec<Vec<i32>> {
        let mut heap = BinaryHeap::new();

        for (shop, shop_content) in &self.rented {
            for (movie_in_shop, price) in shop_content {
                heap.push((*price, *shop, *movie_in_shop));
                if heap.len() > 5 {
                    heap.pop();
                }
            }
        }

        heap.into_sorted_vec()
            .iter()
            .map(|x| vec![x.1, x.2])
            .collect()
    }
}
