using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Threading.Tasks;
using GameCreator.Runtime.Common;
using GameCreator.Runtime.Variables;


namespace MonoBehaviours
{
    public class WeaponAnimations : MonoBehaviour
    {
        [SerializeField] private AnimatorOverrideController[] overrideControllers;
        [SerializeField] private AnimatorOverrider overrider;

        public static bool OneSword;
        public Animator animator;  // Reference to the Animator component
        public LocalListVariables localListVariables;
        
        public void Set(int value)
        {
            //Debug.Log('G');

            overrider.SetAnimations(overrideControllers[value]);
            //Debug.Log('D');

        }

        private void StopOverride()
        {
            animator.runtimeAnimatorController = null;
        }



        // Update is called once per frame
        void Update()
        {
            // Assuming you have a boolean variable called "switchControllers" to determine which controller to use
            Debug.Log(animator.runtimeAnimatorController);
            //Debug.Log(animator);

            // & animator != overrideControllers[0]
            if (!(bool)localListVariables.Get(1))
            {
                Set(0);
                
                //Debug.Log("Sword");

            }
            else
            {
                Set(1);
            }
        }
    }
}
