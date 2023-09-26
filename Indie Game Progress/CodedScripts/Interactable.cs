using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Interactable : MonoBehaviour
{
    private Animator animator;
    public float radius;
    public bool playerInInteractRange;
    public LayerMask whatIsPlayer;
    private bool closed = true;
    private int gold; 
    public Transform[] players;


    private void Awake()
    {
        animator = GetComponent<Animator>();
        gold = Random.Range(10, 50);
    }

    void Update()
    {
        playerInInteractRange = Physics.CheckSphere(transform.position, radius, whatIsPlayer);
        if (playerInInteractRange)
        {
            if (Input.GetKeyDown("e") && closed)
            {
                animator.SetBool("Open", true);

            }
        }
    }
}
