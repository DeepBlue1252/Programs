using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AttributeManager : MonoBehaviour
{
    public float Health;
    public float Strength;
    public float Stamina;
    public float Mana;
    public int Gold;
    private Animator animator;
    

    void Start()
    {
        animator = GetComponent<Animator>();
    }

    void Update()
    {
         if (Health <= 0)
        {
            
            Die();
        }
    }
    
    public void TakeDamage(float amount)
    {
        Health -= amount;
        animator.SetTrigger("hit");
    }

    public void DealDamage(GameObject target)
    {
        var atm = target.GetComponent<AttributeManager>();
        if(atm != null)
        {
            atm.TakeDamage(Strength);
        }
    }

    public void addGold(int worth)
    {
        Gold += worth;
    }

    private void Die()
    {
        GetComponent<EnemyController>().dying = true;
        DisableTriggers();
        animator.SetBool("Die", true);
        Destroy(gameObject, 3f);
    }

    private void DisableTriggers()
    {
        AnimatorControllerParameter[] parameters = animator.parameters;

        for (int i = 0; i < parameters.Length; i++)
        {
            AnimatorControllerParameter parameter = parameters[i];

            if (parameter.type == AnimatorControllerParameterType.Trigger)
            {
                animator.ResetTrigger(parameter.name);
            }
        }
    }
}

