using System.Collections;
using System.Collections.Generic;
using UnityEngine;


namespace MonoBehaviours
{
    public class AnimatorOverrider : MonoBehaviour
    {
        private Animator _animator;

        // Start is called before the first frame update
        private void Awake()
        {
            _animator = GetComponent<Animator>();
        }

        // Update is called once per frame
        public void SetAnimations(AnimatorOverrideController overrideController)
        {
            _animator.runtimeAnimatorController = overrideController;
            //Debug.Log('O');
        }
    }
}