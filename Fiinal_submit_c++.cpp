#include <iostream>
#include <bits/stdc++.h>
#include<stdlib.h>

using namespace std;

#define pb push_back
#define ins insert


struct Ingrediant{
    string name;
    int likes;
    int dislikes;   

    Ingrediant(string given){
        name = given;
        likes = 0;
        dislikes = 0;
    }
    
    bool operator<(const Ingrediant& rhs) const
    {
        return name < rhs.name;
    }

    bool operator==(const Ingrediant& rhs) const
    {
        return name == rhs.name;
    }
};
vector<Ingrediant> ingrediants;
set<string> TotalLikeIgrediants;
set<string> TotalDislikeIgrediants;
set<string> ConstToatalLikeIgrediants;


void getting_inputs(string input_file){
    fstream file;
    file.open(input_file);

    int t;
    file >> t;
    while (t--){
        int l;
        file >> l;

        while (l--){
            string ing; 
            file >> ing;
            TotalLikeIgrediants.ins(ing);

            // auto n = ingrediants.find(ing);
            auto n = std::find (ingrediants.begin(), ingrediants.end(), ing);

            if(n == ingrediants.end()){
                ingrediants.pb(ing);
                auto n = std::find (ingrediants.begin(), ingrediants.end(), ing);
                n->likes++;
            }else { 
                n->likes++;                
            }
        }

        int d;
        file >> d;

        while (d--){
            string ing; 
            file >> ing;
            TotalDislikeIgrediants.ins(ing);

            // auto n = ingrediants.find(ing);
            auto n = std::find (ingrediants.begin(), ingrediants.end(), ing);

            if(n == ingrediants.end()){
                ingrediants.pb(ing); 
                auto n = std::find (ingrediants.begin(), ingrediants.end(), ing);
                n->dislikes++;
            }else { 
                n->dislikes++;                
            }
        }
    }
    file.close();   
    ConstToatalLikeIgrediants = TotalLikeIgrediants;
}

int simulator(set<string> FinalisedIngrediants, string input_file){
    fstream file;
    file.open(input_file);

    int total_customers, happy_customers = 0;
    file >> total_customers;
    cout<<"Total customers : "<<total_customers<<endl;
    while(total_customers--){
        string customer = "happy";
        
        //Iterating customers likes
        int l;
        file >> l;
        for (int i = 0; i < l; i++){
            string ing;
            file >> ing;
            if(FinalisedIngrediants.find(ing) == FinalisedIngrediants.end()){
                customer = "sad";
            }
        }

        //Iterating customers dislikes
        int d;
        file >> d;
            for (int i = 0; i < d; i++){
                string ing;
                file >> ing;
                if(FinalisedIngrediants.find(ing) != FinalisedIngrediants.end()){
                    customer = "sad";
                }
            }

        //Adding cutomer if he's happy
        if(customer == "happy"){
            happy_customers++;
        }

    }
    file.close();

    return happy_customers;
}
void real_algo(float weight){
    for (auto it : ingrediants){
        //remove if 0 likes
        //if dislike >= like remove
        if(it.likes == 0){
            auto n = std::find (ingrediants.begin(), ingrediants.end(), it.name);
            TotalLikeIgrediants.erase(n->name);
       } else if ( it.dislikes/it.likes >= weight){
    //    } else if ( it.dislikes >= it.likes){
        
            auto n = std::find (ingrediants.begin(), ingrediants.end(), it.name);
            TotalLikeIgrediants.erase(n->name);
        }
    }
}

int main() {
    string input_file  = "e_elaborate.in.txt";
    getting_inputs(input_file);


    //Super set of all ingrediants----------
    // cout << "Unique liked ingrediants: " << TotalLikeIgrediants.size() << endl;
    // for (auto &i : TotalLikeIgrediants)
    //     cout << i <<" ";
    // cout << endl;
    // cout << "Unique dis-liked ingrediants: " << TotalDislikeIgrediants.size() << endl;
    // for (auto &i : TotalDislikeIgrediants)
    //     cout << i <<" ";
    // cout << endl;

    //Save to output file-------------------
    // ofstream MyFile("response.txt");
    // MyFile << TotalLikeIgrediants.size();
    // for (auto it : TotalLikeIgrediants)
    //     MyFile << " " <<  it;
    // MyFile.close();

    float max_weight = 1;
    int max_happy_customers = 0;
    //Real algo-----------------------------
    for (float weight = 1; weight < 2; weight += 0.01){
        cout<<"Weight: "<<weight<<endl;

        TotalLikeIgrediants = ConstToatalLikeIgrediants;
        real_algo(weight);

        //Simulator-----------------------------
        int happy_customers = simulator(TotalLikeIgrediants, input_file);
        cout << "Happy customers: " << happy_customers << endl <<endl;

        if(happy_customers > max_happy_customers){
            max_happy_customers = happy_customers;
            max_weight = weight;
        }

    }

    cout<<"Max weight: "<<max_weight<<endl;
    TotalLikeIgrediants = ConstToatalLikeIgrediants;
    real_algo(max_weight);
    int happy_customers = simulator(TotalLikeIgrediants, input_file);
    cout << "Happy customers: " << happy_customers << endl <<endl;

    //Other Ingredianting stuff-------------
    // for (auto it : ingrediants)
    //     cout <<  it.name  << " " << it.likes << " " << it.dislikes << endl;
    return 0;
}
