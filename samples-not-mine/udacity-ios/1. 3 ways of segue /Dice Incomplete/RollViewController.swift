//
//  RollViewController.swift
//  Dice
//
//  Created by Jason Schatz on 11/6/14.
//  Copyright (c) 2014 Udacity. All rights reserved.
//

import UIKit

// MARK: - RollViewController: UIViewController

class RollViewController: UIViewController {
    
    // MARK: Generate Dice Value
    
    /**
    * Randomly generates a Int from 1 to 6
    */
    func randomDiceValue() -> Int {
        // Generate a random Int32 using arc4Random
        let randomValue = 1 + arc4random() % 6
        
        // Return a more convenient Int, initialized with the random value
        return Int(randomValue)
    }

    // MARK: Actions
    
    @IBAction func rollTheDice() {
        // *** 1st method: get other view using storyboard?.instantiateViewController
        var controller: DiceViewController

        controller = self.storyboard?.instantiateViewController(withIdentifier: "DiceViewController") as! DiceViewController

        controller.firstValue = self.randomDiceValue()
        controller.secondValue = self.randomDiceValue()

        present(controller, animated: true, completion: nil)
        
        // *** 2nd method: get another view using segue
        // performSegue(withIdentifier: "rollDice", sender: self)
        // NOTE: pass data to the another view using prepare()
    
        // *** 3rd method: by only using the storyboard by connecting the "Roll The Dice!" button to the another view
        // NOTE: pass data to the another view using prepare()

    }
    
    // NOTE: works only with method 1 and 2
    // override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        
    //     if segue.identifier == "rollDice" {
    //         let controller = segue.destination as! DiceViewController
            
    //         controller.firstValue = randomDiceValue()
    //         controller.secondValue = randomDiceValue()
    //     }
    // }
    
    
}

