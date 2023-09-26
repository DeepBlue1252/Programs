using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ObjectFade : MonoBehaviour
{
    public float fadeSpeed, fadeAmount;
    float originalOpacity;

    Renderer[] renderers;
    Material[] materials;
    public bool doFade = false;

    // Start is called before the first frame update
    void Start()
    {
        renderers = GetComponentsInChildren<Renderer>();
        materials = new Material[renderers.Length];
        for (int i = 0; i < renderers.Length; i++)
        {
            materials[i] = renderers[i].material;
        }

        originalOpacity = materials[0].color.a;
    }

    // Update is called once per frame
    void Update()
    {
        if (doFade)
        {
            FadeNow();
        }
        else
        {
            ResetFade();
        }
    }

    void FadeNow()
    {
        foreach (Material material in materials)
        {
            Color currentColor = material.color;
            Color smoothColor = new Color(currentColor.r, currentColor.g, currentColor.b, Mathf.Lerp(currentColor.a, fadeAmount, fadeSpeed));
            material.color = smoothColor;
        }
    }

    void ResetFade()
    {
        foreach (Material material in materials)
        {
            Color currentColor = material.color;
            Color smoothColor = new Color(currentColor.r, currentColor.g, currentColor.b, Mathf.Lerp(currentColor.a, originalOpacity, fadeSpeed));
            material.color = smoothColor;
        }
    }

}
